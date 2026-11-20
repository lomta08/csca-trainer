import { memo } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';

const remarkPlugins = [remarkMath, remarkGfm];
const rehypePlugins: any[] = [[rehypeKatex, { throwOnError: false, strict: false }]];

/** Markdown with $inline$ and $$display$$ LaTeX. `inline` renders without block paragraphs. */
export const Md = memo(function Md({ children, inline = false, className = '' }: { children: string; inline?: boolean; className?: string }) {
  const Tag = inline ? 'span' : 'div';
  return (
    <Tag className={`${inline ? 'md-inline' : 'md'} ${className}`}>
      <ReactMarkdown
        remarkPlugins={remarkPlugins}
        rehypePlugins={rehypePlugins}
        components={
          inline
            ? { p: ({ children }) => <span>{children}</span> }
            : {
                table: ({ children }) => (
                  <div className="table-wrap">
                    <table>{children}</table>
                  </div>
                ),
              }
        }
      >
        {children}
      </ReactMarkdown>
    </Tag>
  );
});
