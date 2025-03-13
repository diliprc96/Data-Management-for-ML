data_lake/  
│── transactions/            # Source: Financial transactions  
│   ├── csv/                 # Type: Raw CSV files  
│   │   ├── 2025-03-13/      # Date-based partition  
│   │   │   ├── raw/         # Unprocessed data  
│   │   │   ├── processed/   # Cleaned data  
│── customer_support/        # Source: Customer complaints & support logs  
│   ├── json/                # Type: API responses in JSON  
│   │   ├── 2025-03-13/  
│   │   │   ├── raw/  
│   │   │   ├── processed/  
│── web_activity/            # Source: Website/mobile analytics  
│   ├── logs/                # Type: Log files  
│   │   ├── 2025-03-13/  
│   │   │   ├── raw/  
│   │   │   ├── processed/  
│── market_sentiment/        # Source: Social media & competitor analysis  
│   ├── txt/                 # Type: Scraped data stored in text  
│   │   ├── 2025-03-13/  
│   │   │   ├── raw/  
│   │   │   ├── processed/  
