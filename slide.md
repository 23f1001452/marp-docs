---
marp: true
theme: custom-theme
paginate: true
footer: "© 2025 Software Docs — 23f1001452@ds.study.iitm.ac.in"
---

<style>
@theme custom-theme {
  :root {
    --main-color: #2d89ef;
    --heading-font: "Segoe UI", sans-serif;
    --text-color: #222222;
  }

  section {
    font-family: var(--heading-font);
    color: var(--text-color);
    padding: 2rem;
  }

  h1, h2, h3 {
    color: var(--main-color);
  }

  footer {
    font-size: 0.8rem;
    color: #888888;
    margin-top: 1rem;
  }

  /* Custom class for callout boxes */
  .callout {
    border-left: 6px solid var(--main-color);
    padding: 0.6rem 1rem;
    background: rgba(45,137,239,0.05);
    border-radius: 4px;
  }
}
</style>

---
# Product Documentation Presentation
### Marp-based, version-control friendly
**Author / Contact:** 23f1001452@ds.study.iitm.ac.in

---

# What is Marp?

- Markdown → Presentation
- Source controlled (git)
- Export to PDF / PPTX / HTML

---

# Quick Example (Code)

```python
def compute_revenue(transactions):
    """Compute total revenue from transactions list of dicts"""
    return sum(t['qty'] * t['price'] for t in transactions)

# Example
print(compute_revenue([{'qty':10,'price':100.0}, {'qty':5,'price':250.0}]))
