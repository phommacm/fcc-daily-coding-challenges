# HTML Tag Stripper
[View Original Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-15)

## 📝 Challenge Description

Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only **valid HTML**. Tags may be nested and may include attributes; your job is to remove all tags and attributes and return the remaining textual content in document order.

1. The input is an HTML string that may contain nested tags and attributes.
2. Remove all HTML tags (opening, closing and self-closing) and any attributes.
3. Preserve the textual content and the original relative ordering of text nodes.
4. Do **not** add or synthesize whitespace except what already exists in the text nodes. (Trim only if you choose, but examples assume no extra trimming.)
5. Self-closing tags produce no text unless they contain text (which is unusual); they should simply be removed.

**Return Values:**

- A string containing the plain text content with all HTML tags and attributes removed.

---

## 💡 Example

```python
strip_tags('<a href="#">Click here</a>')           # returns "Click here"
strip_tags('<div><p>Hello <b>World</b></p></div>') # returns "Hello World"
strip_tags('<img alt="x"/>No image shown')         # returns "No image shown"
strip_tags('Plain text with no tags')              # returns "Plain text with no tags"
