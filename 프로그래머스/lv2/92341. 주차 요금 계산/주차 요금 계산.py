def get_total_time(time_in, time_out):
    in_hour, in_minute = map(int, time_in.split(":"))
    out_hour, out_minute = map(int, time_out.split(":"))

    total_minute = 0
    # print(time_in, time_out)

    if out_hour == in_hour:
        return out_minute - in_minute

    if out_minute >= in_minute:
        total_minute += out_minute - in_minute
        total_minute += (out_hour - in_hour) * 60
    else:
        if out_hour - in_hour == 1:
            total_minute += 60 - in_minute + out_minute
        else:
            total_minute += (out_hour - in_hour - 1) * 60 + (60 - in_minute + out_minute)

    return total_minute

def get_cost(default_time, default_cost, stand_time, stand_cost, total_minute):
    # print(default_time, default_cost, stand_time, stand_cost, total_minute)
    if total_minute <= default_time:
        return default_cost
    
    else:
        if (total_minute - default_time) % stand_time == 0:
            # print(default_cost, default_time, stand_cost, stand_time)
            # print(default_cost + stand_cost * (total_minute - default_time) // stand_time)
            return default_cost + stand_cost * ((total_minute - default_time) // stand_time)
        else:
            # print(default_cost + stand_cost * ((total_minute - default_time) // stand_time + 1)
    
            return default_cost + stand_cost * (((total_minute - default_time) // stand_time + 1))
    



def solution(fees, records):
    default_time, default_cost, stand_time, stand_cost = fees
    cars_result = {}
    cars = {}
    answer = []
    for record in records:
        # print(cars)
        # print(cars_result)
        time, car_id, cond = record.split(" ")
        if not car_id in cars:
                cars[car_id] = []
                cars[car_id].append(time)
        else:
            cars[car_id].append(time)
            if len(cars[car_id]) == 2:
                if car_id in cars_result:
                    cars_result[car_id] += get_total_time(cars[car_id][0], cars[car_id][1])
                else:
                    cars_result[car_id] = get_total_time(cars[car_id][0], cars[car_id][1])
                cars[car_id] = []
    # print(cars)
    # print(cars_result)
    for key in cars.keys():
        if len(cars[key]) == 1:
            if key in cars_result:
                    cars_result[key] += get_total_time(cars[key][0], '23:59')
            else:
                cars_result[key] = get_total_time(cars[key][0], '23:59')

    # print(cars_result)
    for key in cars_result.keys():
        # print(get_cost(default_time,default_cost,stand_time,stand_cost,cars_result[key]))
        print(get_cost(default_time,default_cost,stand_time,stand_cost,cars_result[key]))
        answer.append((key, get_cost(default_time,default_cost,stand_time,stand_cost,cars_result[key])))
    answer.sort()
    return list(map(lambda x: x[1], answer))