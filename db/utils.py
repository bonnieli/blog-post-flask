def row_to_dict(row):
    result = {}
    for column in row.__table__.columns:
        result[column.name] = getattr(row, column.name)

    return result


def rows_to_list(rows):
    results = []
    for row in rows:
        results.append(row_to_dict(row))
    return results
