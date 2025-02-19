import pandas as pd 

INSTANCE_SIZES = ["nano", "micro", "small", "medium", "large", "xlarge", 
                  "2xlarge", "4xlarge", "8xlarge", "16xlarge", "32xlarge"]

def get_new_size(current_size, change):
    index = INSTANCE_SIZES.index(current_size)
    if change == "smaller" and index > 0:
        return INSTANCE_SIZES[index - 1]
    elif change == "larger" and index < len(INSTANCE_SIZES) - 1:
        return INSTANCE_SIZES[index + 1]
    return current_size

def get_latest_type(instance_type):
    if instance_type.startswith("t2"):
        return "t3"
    elif instance_type.startswith("t3"):
        return "t4"
    elif instance_type.startswith("m5"):
        return "m6"
    return instance_type










def recommend_ec2(instance_name, cpu_usage):
    instance_type, instance_size = instance_name.split(".")





    if cpu_usage < 20:
        new_size = get_new_size(instance_size, "smaller")
        status = "Underutilized"
    elif cpu_usage > 80:
        new_size = get_new_size(instance_size, "larger")
        status = "Overutilized"
    else:
        new_size = instance_size
        instance_type = get_latest_type(instance_type)
        status = "Optimized"

    recommended_instance = f"{instance_type}.{new_size}"

    result = pd.DataFrame([
        [1, instance_name, f"{cpu_usage}%", status, recommended_instance]
    ], columns=["Serial No.", "Current EC2", "CPU Usage  ", "Status  ", "Recommended EC2"])
    
    return result

result_df = recommend_ec2("t2.large", 19)
print(result_df.to_string(index=False))
