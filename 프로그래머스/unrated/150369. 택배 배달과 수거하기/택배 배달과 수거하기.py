def solution(cap, n, deliveries, pickups):

    if len(set(deliveries)) == 1 and len(set(pickups)) == 1:
        return 0
    answer = 0
    while True:
        if len(deliveries) == 0 and len(pickups) == 0:
            break
        

        # if deliveries and pickups and deliveries[-1] == 0 and pickups[-1] == 0:
        #     deliveries.pop()
        #     pickups.pop()
        #     continue
        answer += max(len(deliveries), len(pickups)) * 2
        box_nums = cap

        while deliveries and box_nums != 0:
            if deliveries[-1] <= box_nums:
                box_nums -= deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= box_nums
                break

        box_nums = 0
        while pickups and box_nums != cap:
            if pickups[-1] != 0:
                box_nums += 1
                pickups[-1] -= 1
                
            else:
                pickups.pop()
        
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        
        while pickups and pickups[-1] == 0:
            pickups.pop()


    return answer


# result => 30
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7,[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]))