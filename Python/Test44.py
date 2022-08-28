def split_list(grade: list):
    grade.sort()

    split_index = len(grade)//2

    return (grade[:split_index+1], grade[split_index+1:],)
