def calculate_rate(real_time, real_qty, target_qty, task):
    # assign task to items
    if task == "case_pick":
        item = "cases"
    elif task == "rework":
        item = "pallets"
    # add more conditions as you scale use-cases
    
    # calculate the rates
    real_rate = round((real_qty * 60) / real_time, 1)
    target_rate = target_qty
    
    if real_rate > target_rate:
        return f"You are doing Excellent @ {real_rate} {item}/hr"
    elif real_rate == target_rate:
        return f"You are on Target @ {real_rate} {item}/hr"
    else:
        return f"You are below Target @ {real_rate} {item}/hr"
        