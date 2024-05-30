# RAW
# KH_tables_from_calls_MHKDR.ipynb 

import requests
import pandas as pd
import re

# mhkdr_api = 'https://mhkdr.openei.org/api?action=getSubmissionsForPRIMRE'
# mhkdr_response = requests.get(mhkdr_api)
# mhkdr_response_json = mhkdr_response.json()
# mhkdr_dataframe = pd.DataFrame(mhkdr_response_json)


def find_entry_id(entry_uri):
    '''
    This function takes in the url of a MHKDR entry, and returns the entry_id of that page. 
    The 'entry_id' is the integer at the end of the url, which is unique to each MHKDR entry.
    The regex used in this function relies on the fact that the only number in the url is the id.
    '''
    rule = re.compile(r'\d+')
    matches_rule = rule.findall(entry_uri)
    entry_id = int(matches_rule[0])

    return entry_id


def construct_authors_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "author," connected to an "entry_id" that 
    may be called as a primary key to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among researchers, number of documents 
    attributed to each author.
    '''
    authors_of_entries = list(mhkdr_dataframe['author'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    authors = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])
        
        # Construct "author" column
        num_authors = len(authors_of_entries[i])
        for j in range(0, num_authors):
            entry_ids.append(entry_id)
            authors.append(authors_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'author':authors})
    
    return final_df


def construct_organizations_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "organization," connected to an "entry_id" that 
    may be called as a primary k4ey to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among researchers, number of documents 
    attributed to each author.
    '''
    orgs_of_entries = list(mhkdr_dataframe['organization'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    orgs = list()    # This list will contain duplicate authors when an author contributes to multiple entries
       
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])

        # Construct "author" column
        num_orgs = len(orgs_of_entries[i])
        for j in range(0, num_orgs):
            entry_ids.append(entry_id)
            orgs.append(orgs_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'organization':orgs})
    
    return final_df


def construct_tags_table(mhkdr_dataframe):
    '''
    This function creates a normalized table for the json element "tags," connected to an "entry_id" that 
    may be called as a primary key to join this table to others. This disentangles the nested list structure
    present in the json to enable reporting e.g. associations among researchers, number of documents 
    attributed to each author.
    '''
    tags_of_entries = list(mhkdr_dataframe['tags'])
    landing_page_uris = list(mhkdr_dataframe['URI'])
    
    entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
    tags = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
    for i in range(0, len(mhkdr_dataframe)):
        # Construct "entry_id" - This will be a primary key for all future merge operations.
        entry_id = find_entry_id(landing_page_uris[i])
        
        # Construct "tag" column
        num_tags = len(tags_of_entries[i])
        for j in range(0, num_tags):
            entry_ids.append(entry_id)
            tags.append(tags_of_entries[i][j])
    
    final_df = pd.DataFrame({'entry_id':entry_ids, 'tag':tags})
    
    return final_df



# RAW
# KH_tables_from_calls_Tethys.ipynb

# import requests
# import pandas as pd
# import re

# tethys_api = 'https://tethys.pnnl.gov/api/primre_export'
# tethys_response = requests.get(tethys_api)
# tethys_response_json = tethys_response.json()
# tethys_dataframe = pd.DataFrame(tethys_response_json)


# def find_entry_id(entry_uri):
#     '''
#     This function takes in the url of a MHKDR entry, and returns the entry_id of that page. 
#     The 'entry_id' is the integer at the end of the url, which is unique to each MHKDR entry.
#     The regex used in this function relies on the fact that the only number in the url is the id.
#     '''
#     rule = re.compile(r'\d+')
#     matches_rule = rule.findall(entry_uri)
#     entry_id = int(matches_rule[0])

#     return entry_id


# def construct_authors_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "author," connected to an "entry_id" that 
#     may be called as a primary key to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     authors_of_entries = list(mhkdr_dataframe['author'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     authors = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])
        
#         # Construct "author" column
#         num_authors = len(authors_of_entries[i])
#         for j in range(0, num_authors):
#             entry_ids.append(entry_id)
#             authors.append(authors_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'author':authors})
    
#     return final_df


# def construct_organizations_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "organization," connected to an "entry_id" that 
#     may be called as a primary k4ey to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     orgs_of_entries = list(mhkdr_dataframe['organization'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     orgs = list()    # This list will contain duplicate authors when an author contributes to multiple entries
       
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])

#         # Construct "author" column
#         num_orgs = len(orgs_of_entries[i])
#         for j in range(0, num_orgs):
#             entry_ids.append(entry_id)
#             orgs.append(orgs_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'organization':orgs})
    
#     return final_df


# def construct_tags_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "tags," connected to an "entry_id" that 
#     may be called as a primary key to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     tags_of_entries = list(mhkdr_dataframe['tags'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     tags = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])
        
#         # Construct "tag" column
#         num_tags = len(tags_of_entries[i])
#         for j in range(0, num_tags):
#             entry_ids.append(entry_id)
#             tags.append(tags_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'tag':tags})
    
#     return final_df



# # RAW
# # KH_tables_from_calls_Tethys_Engineering.ipynb

# # import requests
# # import pandas as pd
# # import re

# # tethys_e_api = 'https://tethys-engineering.pnnl.gov/api/primre_export'
# # tethys_e_response = requests.get(tethys_e_api)
# # tethys_e_response_json = tethys_e_response.json()
# # tethys_e_dataframe = pd.DataFrame(tethys_e_response_json)


# def find_entry_id(entry_uri):
#     '''
#     This function takes in the url of a MHKDR entry, and returns the entry_id of that page. 
#     The 'entry_id' is the integer at the end of the url, which is unique to each MHKDR entry.
#     The regex used in this function relies on the fact that the only number in the url is the id.
#     '''
#     rule = re.compile(r'\d+')
#     matches_rule = rule.findall(entry_uri)
#     entry_id = int(matches_rule[0])

#     return entry_id


# def construct_authors_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "author," connected to an "entry_id" that 
#     may be called as a primary key to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     authors_of_entries = list(mhkdr_dataframe['author'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     authors = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])
        
#         # Construct "author" column
#         num_authors = len(authors_of_entries[i])
#         for j in range(0, num_authors):
#             entry_ids.append(entry_id)
#             authors.append(authors_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'author':authors})
    
#     return final_df


# def construct_organizations_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "organization," connected to an "entry_id" that 
#     may be called as a primary k4ey to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     orgs_of_entries = list(mhkdr_dataframe['organization'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     orgs = list()    # This list will contain duplicate authors when an author contributes to multiple entries
       
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])

#         # Construct "author" column
#         num_orgs = len(orgs_of_entries[i])
#         for j in range(0, num_orgs):
#             entry_ids.append(entry_id)
#             orgs.append(orgs_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'organization':orgs})
    
#     return final_df


# def construct_tags_table(mhkdr_dataframe):
#     '''
#     This function creates a normalized table for the json element "tags," connected to an "entry_id" that 
#     may be called as a primary key to join this table to others. This disentangles the nested list structure
#     present in the json to enable reporting e.g. associations among researchers, number of documents 
#     attributed to each author.
#     '''
#     tags_of_entries = list(mhkdr_dataframe['tags'])
#     landing_page_uris = list(mhkdr_dataframe['URI'])
    
#     entry_ids = list()  # This list will contain duplicate entry ids, as it represents the final column that will map to entry
#     tags = list()    # This list will contain duplicate authors when an author contributes to multiple entries
    
#     for i in range(0, len(mhkdr_dataframe)):
#         # Construct "entry_id" - This will be a primary key for all future merge operations.
#         entry_id = find_entry_id(landing_page_uris[i])
        
#         # Construct "tag" column
#         num_tags = len(tags_of_entries[i])
#         for j in range(0, num_tags):
#             entry_ids.append(entry_id)
#             tags.append(tags_of_entries[i][j])
    
#     final_df = pd.DataFrame({'entry_id':entry_ids, 'tag':tags})
    
#     return final_df