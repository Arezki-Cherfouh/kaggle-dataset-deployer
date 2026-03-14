# Kaggle Dataset Uploader

A simple Python utility to automate the creation and uploading of datasets to Kaggle. This tool is designed to bypass the stability issues often found in Kaggle’s web interface by leveraging the official Kaggle API.

## Features

- **Automatic Metadata Generation:** Automatically creates the required `dataset-metadata.json`.
- **Chunked Uploads:** Prevents browser timeouts and "frozen" uploads for large datasets.
- **Configurable:** Easy-to-edit constants for ID, title, and privacy settings.

## Getting Started

### Prerequisites

Ensure you have the Kaggle API library installed:

```bash
pip install -U kaggle
```

### Setup

1. **Get your Token:** Generate an API token from your [Kaggle Account Settings](https://www.kaggle.com/settings).
2. **Configure:** Open `upload_to_kaggle.py` and update the constants at the top:

- `KAGGLE_TOKEN`: Your API token string (e.g., `KGAT_...`).
- `DATASET_ID`: Your target (e.g., `username/dataset-name`).
- `FOLDER_PATH`: The directory containing your files.

### Usage

Run the script from your terminal:

```bash
python3 upload_to_kaggle.py

```

## License

This project is open-source and provided as-is.
