# ZivaID R00 Black-Box Runner

Run the consumer-level verification suite from the repository root:

```text
python -m unittest -v tests/zivaid/test_r00_evidence_engine_blackbox.py
```

The suite uses reserved synthetic identifiers only and must not write to production registers.
