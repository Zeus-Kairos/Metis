#!/bin/bash
"""
Bash script to create a PostgreSQL database and enable the vector extension for Metis.
"""

set -euo pipefail

# Default values
DEFAULT_HOST="localhost"
DEFAULT_PORT="5432"
DEFAULT_USER="postgres"
DEFAULT_DBNAME="metis_db"

# Function to display usage information
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -h, --host HOST        PostgreSQL host (default: $DEFAULT_HOST)"
    echo "  -p, --port PORT        PostgreSQL port (default: $DEFAULT_PORT)"
    echo "  -U, --user USER        PostgreSQL username (default: $DEFAULT_USER)"
    echo "  -W, --password         Prompt for PostgreSQL password"
    echo "  -d, --dbname DBNAME    Database name to create (default: $DEFAULT_DBNAME)"
    echo "  --help                 Display this help message"
    echo ""
    echo "Example: $0 -U postgres -W -d metis_db"
    exit 1
}

# Parse command line arguments
HOST=$DEFAULT_HOST
PORT=$DEFAULT_PORT
USER=$DEFAULT_USER
DBNAME=$DEFAULT_DBNAME
PROMPT_PASSWORD=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--host)
            HOST="$2"
            shift 2
            ;;
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        -U|--user)
            USER="$2"
            shift 2
            ;;
        -W|--password)
            PROMPT_PASSWORD=true
            shift 1
            ;;
        -d|--dbname)
            DBNAME="$2"
            shift 2
            ;;
        --help)
            usage
            ;;
        *)
            echo "Invalid argument: $1"
            usage
            ;;
    esac
done

# Check if psql is installed
if ! command -v psql &> /dev/null; then
    echo "Error: psql is not installed or not in PATH"
    echo "Please install PostgreSQL client tools."
    exit 1
fi

# Handle password input
if [ "$PROMPT_PASSWORD" = true ]; then
    # Prompt for password once and set as environment variable
    read -s -p "Enter PostgreSQL password for user '$USER': " PGPASSWORD
    echo
    export PGPASSWORD
else
    # Set empty password by default if not prompting
    PGPASSWORD=""
    export PGPASSWORD
fi

# Build connection string for psql
PSQL_CONN="-h $HOST -p $PORT -U $USER"

# Test connection to PostgreSQL server
echo "Testing connection to PostgreSQL server at $HOST:$PORT..."
if ! psql $PSQL_CONN -d postgres -c "\q" 2>/dev/null; then
    echo "Error: Could not connect to PostgreSQL server"
    echo "Please check your host, port, and credentials."
    exit 1
fi

echo "Connected to PostgreSQL server successfully!"

# Check if database already exists
echo "\nChecking if database '$DBNAME' exists..."
if psql $PSQL_CONN -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname = '$DBNAME'" | grep -q 1; then
    echo "Database '$DBNAME' already exists."
else
    echo "Creating database '$DBNAME'..."
    psql $PSQL_CONN -d postgres -c "CREATE DATABASE $DBNAME"
    echo "Database '$DBNAME' created successfully!"
fi

# Connect to the database and enable vector extension
echo "\nEnabling vector extension in database '$DBNAME'..."
psql $PSQL_CONN -d "$DBNAME" -c "CREATE EXTENSION IF NOT EXISTS vector"

# Verify vector extension is enabled
echo "\nVerifying vector extension..."
if psql $PSQL_CONN -d "$DBNAME" -tAc "SELECT extname FROM pg_extension WHERE extname = 'vector'" | grep -q vector; then
    echo "Vector extension is successfully enabled!"
else
    echo "Error: Vector extension is not enabled."
    exit 1
fi

echo "\n🎉 Database setup completed successfully!"
echo ""
echo "Database: $DBNAME"
echo "Host: $HOST"
echo "Port: $PORT"
echo "User: $USER"
echo ""
echo "Add this to your .env file:"
echo "DB_URI=postgresql://$USER@$HOST:$PORT/$DBNAME"
echo ""
echo "If you set a password, include it in the DB_URI like:"
echo "DB_URI=postgresql://$USER:your_password@$HOST:$PORT/$DBNAME"
