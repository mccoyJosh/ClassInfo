
expected_subnet_address = "127.0.0.1"

def connect_sql_database(ip):
    port = "3000"
    if ip == expected_subnet_address + ":" + port:
        return True
    return False

def connect_neo4j_database(ip):
    port = "3800"
    if ip == expected_subnet_address + ":" + port:
        return True
    return False


def connect_calc_service(ip):
    port = "4000"
    if ip == expected_subnet_address + ":" + port:
        return True
    return False

def connect_front_end_service(ip):
    port = "7777"
    if ip == expected_subnet_address + ":" + port:
        return True
    return False

def sql_read():
    return "Db1", (1, "Accounts", ("Id", "Name", "Amount", "Rank"), [(1, "Bingus", 20091, "Fisher"),(1, "Bono", 90, "Expert"), (1, "Linguiny", 199982, "Noob"), (1, "Monolopy", 90019, "Fish Salesman")])


def neo_read():
    return "Db1", (1, "Names", ["Bingus", "Bono", "Linguiny", "Monolopy"], [2, 1, 3, 4, 5, 1, 5, 12, 11, 1])


def calc_call_total_and_highest_rank(accounts):
    total = 0
    highest_rank = ''
    highest_rank_val = 0
    rank_map = {
        'Noob': 1,
        'Expert': 2,
        'Fisher': 3,
        'Fish Salesman': 4
    }
    for account in accounts:
        temp_amount = account[2]
        rank = account[3]
        total += temp_amount
        if rank_map[rank] > highest_rank_val:
            highest_rank = rank
            highest_rank_val = rank_map[rank]
    return total, highest_rank


def call_neo_calc(neo_results):
    connection_total = 0
    for nr in neo_results:
        connection_total += nr
    return connection_total


def create_html(title, heading, paragraph):
    example_html = f'''
<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
    
    <h1>{heading}</h1>
    <p>{paragraph}</p>
    
    </body>
</html> 
    '''
    return example_html