def save_new_data_type(test_type, dt_id, filename='new_dt_ids'):
    with open(filename, 'a') as f:
        new_id_record = '\n{}: {}'.format(test_type, dt_id)
        f.write(new_id_record)
