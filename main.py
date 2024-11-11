
import os
import pickle as pkl
import Config as c
import FinalTemplate as template_creation
import PrepareData as createData
import ebdba_template_creation


#DB='xLang'

def Create_EBDBA_Template_for_every_user(all_user_data):
    for _user in c.users:
        ebdba_template_name = f'EBDBA_Template\\{c.DB}\\USER{str(_user)}_EBDBA'
        print('Create_EBDBA_Template_for_every_user for user :', _user)
        if not os.path.isfile(ebdba_template_name):
            ebdba_template_creation.get_ebdba_Template(_user, user_all_file_data=all_user_data[_user])

def Create_final_template(user,data):
    return template_creation.CreateFinalTemplate(user, data)

if __name__ == '__main__':
    #file_name = 'all_featured_data_'+c.DB
    if not os.path.isfile(c.data_file_name):
        print('Data is not prepared.')
        print('Data prepration is started...')
        # if DB=='xLang':
        #     file_name='all_featured_data_xLang'
        #     userdata = createData_xLang.get_all_user_data()
        # else:
        userdata = createData.get_all_user_data()

        with open(c.data_file_name, 'wb') as file:
            pkl.dump(userdata,file)
        print('Data prepration is completed.')
    else:
        print('Data is already prepared')
        print('Load data from pikle..')
        with open(c.data_file_name, 'rb') as file:
            userdata =pkl.load(file)
        print('Data load completed')

    print('Length of data',len(userdata))

    if not os.path.isfile(c.key_file_name):
        print("UserKey is being creted of size ",c.KeySize)
        createData.GenerateRandomKeyForUsers()
    else:
        print("Key Already present of size ",c.KeySize)

    print('EBDBA template creation for all available user is started. See the file used in template creation is config file')
    Create_EBDBA_Template_for_every_user(userdata)
    print('EBDBA template are created. You can check them in EBDBA_Template folder.')

    for user in c.users:
        ebdba_template_name = f'EBDBA_Template\\{c.DB}\\USER{str(user)}_EBDBA'
        with open(ebdba_template_name, 'rb') as f:
            ebdba_template = pkl.load(f)
        template_file_name=f"Final_Template\\{c.DB}\\Template_{str(user)}.txt"
        if not os.path.isfile(template_file_name):
            print('Final template is being created for user ', user)
            template=Create_final_template(user,ebdba_template)
            with open(template_file_name, "w") as text_file:
                text_file.write(template)
            print('Final template is created for user ', user)