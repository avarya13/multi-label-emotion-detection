from datasets import load_dataset


def download_data(cfg):
    """Download dataset from Hugging Face and save to target_dir"""
    dataset = load_dataset(cfg.data_url)
    target_path = cfg.data_dir
    dataset.save_to_disk(target_path)
    print(f"Dataset saved to {target_path}")


if __name__ == "__main__":
    download_data()
