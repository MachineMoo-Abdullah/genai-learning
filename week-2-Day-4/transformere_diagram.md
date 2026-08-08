# Transformer Architecture Diagrams

## 1. Transformer Architecture

```mermaid
flowchart TD

    A[Input Text] --> B[Tokenization]
    B --> C[Token IDs]
    C --> D[Token Embeddings]

    D --> E[Positional Encoding]

    E --> F[Multi-Head Self-Attention]

    F --> G[Add & Norm]

    G --> H[Feed Forward Network]

    H --> I[Add & Norm]

    I --> J[Transformer Block]

    J --> K[Repeated Transformer Blocks]

    K --> L[Linear Layer]

    L --> M[Softmax]

    M --> N[Output Tokens]