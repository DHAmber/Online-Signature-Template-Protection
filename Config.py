import os.path

NormalizedFlag=False

DB='Task2'
data_file_type='.txt'
db_root=f"D:\\Amber\\Database\\Signature_DB\\database in uniform format\\all data Task2\\"
user_number_start_from=1
user_number_start_to=2

data_file_name = f'all_featured_data_{DB}'
key_file_name=f'UsersKey_{DB}.csv'
#keys = ['X', 'Y', 'T', 'B', 'Az', 'Al', 'P', 'path_tangent_angle', 'path_velocity', 'log_curvature_radius','total_acceleration']
keys = ['X', 'Y', 'T', 'Az', 'Al', 'P', 'path_tangent_angle', 'path_velocity', 'log_curvature_radius','total_acceleration']


users=[]
Genuine=[]
Fake=[]

for i in range (user_number_start_from,user_number_start_to+1):
    if os.path.exists(db_root+f'USER{i}_5{data_file_type}'):
        users.append(i)

KeySize=32
for i in range(1,10):
    Genuine.append(i)
    Fake.append(i+30)

files_to_create_ebdba_template=[]
for i in Genuine:
    files_to_create_ebdba_template.append(i)

def createDirectory():

    for folder in ['Final_Template','EBDBA_Template','Results']:
        directory = f'{folder}\\{DB}'
        if not os.path.exists(directory):
            os.makedirs(directory)
createDirectory()