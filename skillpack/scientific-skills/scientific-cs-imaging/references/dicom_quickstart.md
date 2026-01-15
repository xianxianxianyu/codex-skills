# DICOM Quickstart (pydicom-oriented)

## Minimal goals
1) Read one DICOM file
2) Extract key tags
3) Extract pixel array (if present)
4) Save a preview image + a metadata table

## Minimal snippet
```python
import pydicom
import numpy as np

ds = pydicom.dcmread("sample.dcm")
tags = {
  "Modality": getattr(ds, "Modality", None),
  "StudyDate": getattr(ds, "StudyDate", None),
  "Rows": getattr(ds, "Rows", None),
  "Columns": getattr(ds, "Columns", None),
}

pixel = ds.pixel_array if "PixelData" in ds else None
```

## Anonymization note
Treat these as sensitive by default: PatientName, PatientID, AccessionNumber, StudyInstanceUID, etc.

