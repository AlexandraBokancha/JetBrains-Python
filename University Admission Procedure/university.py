max_number = int(input())
department_applicants = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

with open('applicants.txt', 'r') as f:
    all_applicants = [line.strip().split() for line in f.readlines()]


def calculate_score(department, scores):
    if department == 'Biotech':
        return (float(scores[0]) + float(scores[1])) / 2
    elif department == 'Physics':
        return (float(scores[0]) + float(scores[2])) / 2
    elif department == 'Engineering':
        return (float(scores[2]) + float(scores[3])) / 2


def select_best_candidate(priority):

    global all_applicants
    final_result = []
    accepted_applicants = []

    for department, applicants in department_applicants.items():
        if len(applicants) > max_number:
            continue
        if department == 'Chemistry':
            final_result = sorted(all_applicants, key=lambda x: (-(max(float(x[3]), float(x[6]))), x[0], x[1]))
        elif department == 'Mathematics':
            final_result = sorted(all_applicants, key=lambda x: (-(max(float(x[4]), float(x[6]))), x[0], x[1]))
        elif department == 'Biotech' or department == 'Physics' or department == 'Engineering':
            final_result = sorted(all_applicants,
                                  key=lambda x: (-max(calculate_score(department, x[2:6]), int(x[6])), x[0], x[1]))

        for candidate in final_result:
            if department == candidate[priority]:
                if len(applicants) < max_number:
                    if candidate in accepted_applicants:
                        continue
                    if department == 'Chemistry':
                        department_applicants[department].append(
                            ' '.join(candidate[:2]) + ' ' + str(max(candidate[3], candidate[6])))
                    elif department == 'Mathematics':
                        department_applicants[department].append(
                            ' '.join(candidate[:2]) + ' ' + str(max(candidate[4], candidate[6])))
                    elif department == 'Biotech' or department == 'Physics' or department == 'Engineering':
                        department_applicants[department].append(
                            f"{candidate[0]} {candidate[1]} {max(calculate_score(department, candidate[2:6]), int(candidate[6]))}")

                    # save accepted applicants
                    accepted_applicants.append(candidate)

            # remove accepted candidates from main list
            all_applicants = [a for a in all_applicants if str(a) not in [str(aa) for aa in accepted_applicants]]


for priority in range(7, 10):
    select_best_candidate(priority)

for department in department_applicants:
    department_applicants[department] = sorted(department_applicants[department],
                                               key=lambda x: (-float(x.split()[2]), x.split()[0], x.split()[1]))

    with open(f"{department.lower()}.txt", "w") as f:
        for applicant in department_applicants[department]:
            f.write(applicant + "\n")
