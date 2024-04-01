def calculate_total_times(df):
    finish_df = df[df['process_step'] == "confirm"]
    start_df = df[df['process_step'] == "start"]

    total_times = []

    for visit_id in finish_df['visit_id_numbers'].unique():
        finish_time = finish_df[(finish_df['visit_id_numbers'] == visit_id)].iloc[-1]['date_time']

        start_times_before_confirm = start_df[(start_df['visit_id_numbers'] == visit_id) & (start_df['date_time'] < finish_time)]
        if not start_times_before_confirm.empty:
            starting_time = start_times_before_confirm.iloc[-1]['date_time']
            total_time = finish_time - starting_time
            total_times.append(total_time)

    return total_times

def calculate_time_differences_step(test_finish_df, first_step, next_step):
    time_differences = []
    for client_id, group in test_finish_df.groupby('visit_id_numbers'):
        for i in range(len(group) - 1):
            if group.iloc[i]['step_value'] == first_step and group.iloc[i + 1]['step_value'] == next_step:
                time_diff = group.iloc[i + 1]['date_time'] - group.iloc[i]['date_time']
                time_differences.append(time_diff.total_seconds())
    return time_differences

def check_next_step_errors(df):
    error_count = 0
    for client_id, group in df.groupby('visit_id_numbers'):
        for i in range(len(group) - 1):
            if group.iloc[i]['step_value'] > group.iloc[i + 1]['step_value']:
                error_count += 1
                break
    return error_count
