# AI Sales Proposal Generator - Architecture

## Overview

The application uses a three-stage LLM prompt-chaining architecture.

```text
                    User Input
                        |
                        v
                +---------------+
                | Client Input  |
                +---------------+
                        |
                        v
                +---------------+
                |    LLM #1     |
                | Client Analysis|
                +---------------+
                        |
                        v
                 Structured JSON
                        |
                        v
                +---------------+
                |    LLM #2     |
                | Solution Design|
                +---------------+
                        |
                        v
                Proposed Solution
                        |
                        v
                +---------------+
                |    LLM #3     |
                | Proposal Writer|
                +---------------+
                        |
                        v
                 Final Proposal
                        |
                        v
                    Streaming
                        |
                        v
                  Gradio UI
                        |
                        +---------> Markdown
                        |
                        +---------> TXT