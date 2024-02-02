from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'D:\\Gokul_Sivakumar\\EnergyInsightApp\\EnergyInsight\\databases\\credentials.json')
project_id = 'theta-cell-406519'
dataset_name = 'gokul_energy_data'

class AdminModel:
    @staticmethod
    def get_all_users():
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'users'
        query = f'''
            SELECT *
            FROM `{project_id}.{dataset_name}.{table_name}`
        '''

        query_job = client.query(query)
        users = query_job.result()

        return users

    @staticmethod
    def delete_user(user_name):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'users'
        query = f'''
            DELETE
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE UserName = @user_name
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
            ]
        )

        try:
            query_job = client.query(query, job_config=job_config)
            query_job.result()  # Waits for the job to complete
            print(f"User {user_name} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {str(e)}")

    @staticmethod
    def get_user_by_name(user_name):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'users'
        query = f'''
            SELECT *
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE UserName = @user_name
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("user_name", "STRING", user_name),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        result_iterator = query_job.result()

        try:
            user_data = next(result_iterator)
            return user_data
        except StopIteration:
            # No results found
            return None

    
    @staticmethod
    def get_admin_by_name_and_password(admin_name, password):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'admins'
        query = f'''
            SELECT *
            FROM `{project_id}.{dataset_name}.{table_name}`
            WHERE admin_name = @admin_name AND password = @password
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("admin_name", "STRING", admin_name),
                bigquery.ScalarQueryParameter("password", "STRING", password),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        result_iterator = query_job.result()

        try:
            admin_data = next(result_iterator)
            return admin_data
        except StopIteration:
            # No results found
            return None
        
    @staticmethod
    def create_admin(admin_name, password):
        client = bigquery.Client(credentials=credentials, project=project_id)
        table_name = 'admins'

        query = f'''
            INSERT INTO `{project_id}.{dataset_name}.{table_name}` (admin_name, password)
            VALUES (@admin_name, @password)
        '''

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("admin_name", "STRING", admin_name),
                bigquery.ScalarQueryParameter("password", "STRING", password),
            ]
        )

        query_job = client.query(query, job_config=job_config)
        query_job.result()  # Wait for the query to complete

        print("\nAdmin registered successfully.")    
    
    
