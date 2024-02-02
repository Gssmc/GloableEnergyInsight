from google.cloud import bigquery
from google.oauth2 import service_account
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

credentials = service_account.Credentials.from_service_account_file(
    'D:\\Gokul_Sivakumar\\EnergyInsightApp\\EnergyInsight\\databases\\credentials.json')
project_id = 'theta-cell-406519'
dataset_name = 'gokul_energy_data'

class VisualizationModel:

    @staticmethod
    def plot_global_energy_consumption(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, 
            coal_consumption + oil_consumption + gas_consumption as total_energy_consumption
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()


        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='total_energy_consumption', hue='country', data=data)
        plt.title('Global Energy Consumption Over Years')
        plt.xlabel('Year')
        plt.ylabel('Energy Consumption(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
        

    @staticmethod
    def plot_global_energy_production(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, 
            coal_production + oil_production + gas_production as total_energy_production
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='total_energy_production', hue='country', data=data)
        plt.title('Global Energy Production Over Years')
        plt.xlabel('Year')
        plt.ylabel('Energy Production(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()    

    @staticmethod
    def plot_energy_consumption_between_two_countries(selected_countries):
        if len(selected_countries) != 2:
            print("Please select exactly two countries for this visualization.")
            return

        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, coal_consumption + oil_consumption + gas_consumption as total_energy_consumption
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Filter data for the selected countries
        data = data[data['country'].isin(selected_countries)]

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='total_energy_consumption', hue='country', data=data)
        plt.title('Energy Consumption Between Two Countries Over Years')
        plt.xlabel('Year')
        plt.ylabel('Energy Consumption(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_global_coal_consumption(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, coal_consumption
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()
        

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='coal_consumption', hue='country', data=data)
        plt.title('Global Coal Energy Consumption Over Years')
        plt.xlabel('Year')
        plt.ylabel('Coal Energy Consumption(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_global_coal_production(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, coal_production
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='coal_production', hue='country', data=data)
        plt.title('Global Coal Energy Production Over Years')
        plt.xlabel('Year')
        plt.ylabel('Coal Energy Production(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_global_oil_consumption(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, oil_consumption
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='oil_consumption', hue='country', data=data)
        plt.title('Global Oil Energy Consumption Over Years')
        plt.xlabel('Year')
        plt.ylabel('Oil Energy Consumption(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_global_oil_production(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, oil_production
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='oil_production', hue='country', data=data)
        plt.title('Global Oil Energy Production Over Years')
        plt.xlabel('Year')
        plt.ylabel('Oil Energy Production(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()  


    @staticmethod
    def plot_global_gas_consumption(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, gas_consumption
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='gas_consumption', hue='country', data=data)
        plt.title('Global Gas Energy Consumption Over Years')
        plt.xlabel('Year')
        plt.ylabel('Gas Energy Consumption(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()  


    @staticmethod
    def plot_global_gas_production(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT year, country, gas_production
            FROM `{project_id}.{dataset_name}.energy_data`
            WHERE country IN UNNEST(@selected_countries)
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='year', y='gas_production', hue='country', data=data)
        plt.title('Global Gas Energy Production Over Years')
        plt.xlabel('Year')
        plt.ylabel('Gas Energy Production(J)')
        plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()


    @staticmethod
    def plot_compare_energy_consumption_with_population(selected_countries):
        # Fetch data from BigQuery
        query = f"""
            SELECT
            year,
            country,
            coal_consumption + oil_consumption + gas_consumption AS total_energy_consumption,
            population
            FROM
            `{project_id}.{dataset_name}.energy_data`
            WHERE
            country IN UNNEST(@selected_countries);
        """

        client = bigquery.Client(credentials=credentials, project=project_id)
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries)
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        data = results.to_dataframe()

        # Create subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Plotting for energy consumption
        sns.barplot(x='year', y='total_energy_consumption', hue='country', data=data, palette='viridis', ax=ax1)
        ax1.set_title('Energy Consumption Over Years')
        ax1.set_ylabel('Energy Consumption')
        ax1.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax1.tick_params(axis='x', rotation=45)  # Rotate x-axis labels

        # Plotting for population
        sns.barplot(x='year', y='population', hue='country', data=data, palette='muted', alpha=0.7, ax=ax2)
        ax2.set_title('Population Over Years')
        ax2.set_xlabel('Year')
        ax2.set_ylabel('Population')
        ax2.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.tick_params(axis='x', rotation=45)  # Rotate x-axis labels

        plt.tight_layout()
        plt.show()






















class EnergyModel:
    @staticmethod
    def energy_compare_by_date_for_countries(date_to_compare, selected_countries):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'energy_data'
        query = f'''
            SELECT
                COALESCE(country, 'Unknown') AS country,
                SUM(coal_consumption + oil_consumption + gas_consumption) AS total_consumption,
                SUM(coal_production + oil_production + gas_production) AS total_production
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE (CAST(year AS STRING) = @date_to_compare OR year IS NULL)
                AND (country IN UNNEST(@selected_countries) OR country IS NULL)
            GROUP BY country
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("date_to_compare", "STRING", date_to_compare),
                bigquery.ArrayQueryParameter("selected_countries", "STRING", selected_countries),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()

        if not results.total_rows:
            print(f"No matching records found for year {date_to_compare} and selected countries.")
        else:
            return results

    @staticmethod
    def get_energy_summary(country):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'energy_data'
        query = f'''
            SELECT
                COALESCE(SUM(coal_consumption + oil_consumption + gas_consumption), 0) AS total_consumption,
                COALESCE(AVG(coal_consumption + oil_consumption + gas_consumption), 0) AS average_consumption,
                COALESCE(MIN(coal_consumption + oil_consumption + gas_consumption), 0) AS min_consumption,
                COALESCE(MAX(coal_consumption + oil_consumption + gas_consumption), 0) AS max_consumption,
                COALESCE(SUM(coal_production + oil_production + gas_production), 0) AS total_production,
                COALESCE(AVG(coal_production + oil_production + gas_production), 0) AS average_production,
                COALESCE(MIN(coal_production + oil_production + gas_production), 0) AS min_production,
                COALESCE(MAX(coal_production + oil_production + gas_production), 0) AS max_production
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE country = @country
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("country", "STRING", country)]
        )

        query_job = client.query(query, job_config=job_config)
        result = query_job.result()

        # Check if any rows were returned
        rows = list(result)
        if not rows:
            return None  # Or raise an exception, depending on your logic

        return rows[0]

    @staticmethod
    def get_energy_data_by_year(country, year):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'energy_data'
        query = f'''
            SELECT
                population,
                coal_consumption,
                coal_production,
                oil_consumption,
                oil_production,
                gas_consumption,
                gas_production
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE country = @country AND year = @year
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("country", "STRING", country),
                bigquery.ScalarQueryParameter("year", "INT64", year),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        results = query_job.result()

        if not results.total_rows:
            print(f"No matching records found for country {country} and year {year}.")
        else:
            return [row for row in results]

    @staticmethod
    def get_global_energy_data():
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'energy_data'
        query = f'''
            SELECT
                SUM(coal_consumption + oil_consumption + gas_consumption) AS total_consumption,
                AVG(coal_consumption + oil_consumption + gas_consumption) AS average_consumption,
                SUM(coal_production + oil_production + gas_production) AS total_production,
                AVG(coal_production + oil_production + gas_production) AS average_production
            FROM `{project_id}.{dataset_name}.{table_name}`
        '''

        query_job = client.query(query)

        # Iterate over the result rows and get the first row if it exists
        rows = list(query_job)
        row = rows[0] if rows else None

        return row
    
    


class UserModel:
    def get_user_by_name(user_name, password):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'users'
        query = f'''
            SELECT * FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE UserName = @user_name AND Password = @password
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
                bigquery.ScalarQueryParameter("password", "STRING", password),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        result = query_job.result()

        # Check if any rows were returned
        rows = list(result)
        if not rows:
            return None  # Or raise an exception, depending on your logic

        return rows[0]

    @staticmethod
    def create_user(user_name, password, email, country):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'users'
        query = f'''
            INSERT INTO `{project_id}.{dataset_name}.{table_name}` (UserName, Password, Email, Country)
            VALUES (@user_name, @password, @email, @country)
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
                bigquery.ScalarQueryParameter("password", "STRING", password),
                bigquery.ScalarQueryParameter("email", "STRING", email),
                bigquery.ScalarQueryParameter("country", "STRING", country),
            ]
        )

        query_job = client.query(query, job_config=job_config)

    @staticmethod
    def update_password(user_name, new_password):
        client = bigquery.Client(credentials=credentials, project=project_id)

        table_name = 'users'
        query = f'''
            UPDATE `{project_id}.{dataset_name}.{table_name}`
            SET Password = @new_password
            WHERE UserName = @user_name
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("new_password", "STRING", new_password),
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
            ]
        )

        query_job = client.query(query, job_config=job_config)

    @staticmethod
    def update_email(user_name, new_email):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'users'
        query = f'''
            UPDATE `{project_id}.{dataset_name}.{table_name}`
            SET Email = @new_email
            WHERE UserName = @user_name
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("new_email", "STRING", new_email),
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
            ]
        )

        query_job = client.query(query, job_config=job_config)

    @staticmethod
    def update_country(user_name, new_country):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'users'
        query = f'''
            UPDATE `{project_id}.{dataset_name}.{table_name}`
            SET Country = @new_country
            WHERE UserName = @user_name
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("new_country", "STRING", new_country),
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
            ]
        )

        try:
            query_job = client.query(query, job_config=job_config)
            query_job.result()  # Waits for the job to complete
            return "Update successful"
        except Exception as e:
            return f"Update failed: {str(e)}"

