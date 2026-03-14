import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

# === CONFIGURATION (Edit these) ===
KAGGLE_TOKEN = "KGAT_4b1373e7ebd0760a75e862ff02c4ed3e"
DATASET_ID   = "arezkicherfouh/noobai-lora" # format: username/slug
TITLE        = "NoobAI LoRA Dataset"
FOLDER_PATH  = "./my_training_data"           # The folder containing your data
IS_PRIVATE   = True                           # Set to False for public
# ==================================

def upload_to_kaggle():
    # 1. Setup Authentication
    os.environ['KAGGLE_API_TOKEN'] = KAGGLE_TOKEN
    api = KaggleApi()
    api.authenticate()

    if not os.path.exists(FOLDER_PATH):
        print(f"Error: The folder '{FOLDER_PATH}' does not exist.")
        return

    # 2. Create the dataset-metadata.json file automatically
    metadata = {
        "title": TITLE,
        "id": DATASET_ID,
        "licenses": [{"name": "CC0-1.0"}]
    }

    meta_file_path = os.path.join(FOLDER_PATH, 'dataset-metadata.json')
    
    with open(meta_file_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"✓ Metadata created: {DATASET_ID}")

    # 3. Upload the Dataset
    print(f"Starting upload from: {FOLDER_PATH}...")
    
    # create_new parameters:
    # folder, dir_mode='zip' (zips it up), public/private flag, quiet mode
    api.dataset_create_new(
        FOLDER_PATH, 
        dir_mode='zip', 
        public=not IS_PRIVATE, 
        quiet=False
    )

    print("\n✓ Process Finished! Check your Kaggle datasets page.")

if __name__ == "__main__":
    upload_to_kaggle()