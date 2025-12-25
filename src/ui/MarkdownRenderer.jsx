import React, { useEffect, useRef } from 'react';
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';

// Configure marked to use highlight.js for code blocks
marked.setOptions({
  highlight: function(code, lang) {
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
    return hljs.highlightAuto(code).value;
  },
  breaks: true,
  gfm: true,
});

const MarkdownRenderer = ({ content }) => {
  const markdownRef = useRef(null);

  useEffect(() => {
    if (markdownRef.current && content) {
      // Set the HTML content
      markdownRef.current.innerHTML = marked(content);
      
      // Add event listeners to links to open in new tab
      const links = markdownRef.current.querySelectorAll('a');
      links.forEach(link => {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
      });
    }
  }, [content]);

  if (!content) return null;

  return (
    <div 
      ref={markdownRef}
      className="markdown-renderer"
      style={{
        lineHeight: '1.6',
        fontSize: '16px',
        width: '100%',
        display: 'block',
      }}
    />
  );
};

export default MarkdownRenderer;