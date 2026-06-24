# InsightPro Analytics Platform

## Overview
InsightPro is a lightweight, high-performance Business Intelligence (BI) dashboard built with Python and Flask. It serves as an analytics platform for processing, aggregating, and visualizing mock sales, product, and customer data in real-time. Designed with a modular architecture, InsightPro focuses on robust backend data aggregation using Pandas, coupled with an interactive, responsive frontend experience built with vanilla JavaScript and Chart.js.

## Features
- **Multi-Page Architecture**: Distinct views for Dashboard, Revenue Analytics, Product Analytics, Customer Analytics, and Reports.
- **Dynamic Filtering**: Global date range selection to filter analytics across all views dynamically.
- **Data Visualization**: Clean, responsive, and animated charts (Line, Bar, Doughnut) powered by Chart.js.
- **Stateful Navigation**: Smart "Page-Aware" Javascript routing that fetches data strictly for the currently active page.
- **Automated Seeding**: Integrated Faker and SQLite setup to instantly scaffold 5,000+ realistic transaction records.
- **CSV Exports**: Built-in backend endpoint for exporting tabular report data seamlessly.

## Tech Stack
- **Backend**: Python 3, Flask
- **Data Layer**: SQLite3
- **Data Processing**: Pandas
- **Frontend**: HTML5, CSS3 (Custom Design System with CSS Variables), Vanilla JS
- **Visualizations**: Chart.js
- **Icons**: Font Awesome 6

## Dashboard Modules
* **Dashboard**: Executive summary featuring top KPI cards, revenue trends, top 10 products, category splits, and top customers table.
* **Revenue Analytics**: Deep dive into revenue metrics, featuring month-over-month growth charts and regional performance.
* **Product Analytics**: Evaluation of product metrics via category distribution and comprehensive performance tables indicating units sold and average unit prices.
* **Customer Analytics**: Regional spending distributions and segment analysis (Enterprise vs. SMB vs. Consumer).
* **Reports**: A paginated, tabular view of raw transactional data, ready for export.

## Project Structure
```text
InsightPro/
├── app.py                      # Application entry point
├── config.py                   # Environment configuration variables
├── database/                   
│   ├── db_helper.py            # SQLite connection logic
│   ├── db_init.py              # Script to execute schema creation
│   └── schema.sql              # Database schema definition
├── routes/                     
│   ├── api_routes.py           # REST API endpoints returning JSON
│   └── dashboard_routes.py     # HTML Template rendering endpoints
├── services/                   
│   └── analytics_service.py    # Core business logic and Pandas aggregations
├── static/                     
│   ├── css/style.css           # Global design system
│   └── js/main.js              # Frontend controller and Chart.js factory
├── templates/                  # Jinja2 HTML templates
├── seed_data.py                # Database population script
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git tracking rules
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/insightpro.git
   cd insightpro
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

InsightPro uses SQLite for local development. To create the database and populate it with 5,000+ sample records:

```bash
python seed_data.py
```

*This will automatically read `database/schema.sql`, construct the tables, and generate realistic sample data ending at the current calendar date.*

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```
2. **Access the platform:**
   Open a web browser and navigate to `http://127.0.0.1:5000`

## API Endpoints
The platform exposes several read-only REST endpoints that accept `start_date` and `end_date` query parameters (e.g., `?start_date=2024-01-01&end_date=2025-01-01`):

- `GET /api/kpis`
- `GET /api/revenue-trend`
- `GET /api/product-sales`
- `GET /api/sales-by-category`
- `GET /api/top-customers`
- `GET /api/export-csv`

## Future Improvements
- **Authentication**: Integrate Flask-Login or JWT for secure, user-scoped data access.
- **Predictive Analytics**: Incorporate Prophet or ARIMA models for revenue forecasting.
- **Advanced Exporting**: Implement PDF generation for print-ready executive summaries.


