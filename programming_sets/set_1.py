def savings(gross_pay, tax_rate, expenses):
    return int(gross_pay-(gross_pay*tax_rate))-expenses
def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    waste = total_material - total_consumed
    return f"{waste}{material_units}"
def interest(principal, rate, period):
    return principal+int(principal*rate*period)
