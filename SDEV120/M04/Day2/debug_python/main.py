import network as n

def main():
    sql_results = None
    neo_4j_results = None
    sql_ip = "127.0.0.1:3030"
    neo_ip = "127.0.0.1:3800"
    calc_ip = "127.0.0.1:4000"
    front_ip = "127.0.0.1:7777"
    print("ATTEMPTING TO CONNECT")

    if n.connect_sql_database(sql_ip):
        sql_results = n.sql_read()


    if n.connect_neo4j_database(neo_ip):
        neo_4j_results = n.neo_read()

    if not n.connect_calc_service(calc_ip):
        print("ERROR: FAILED TO CONNECT TO THE CALCULATION SERVICE")
        exit(0)

    if not n.connect_front_end_service(front_ip):
        print("ERROR: FAILED TO CONNECT TO THE FRONT END SERVICE")
        exit(0)

    print("CONNECTIONS COMPLETE")

    user_totals_and_highest_rank = n.calc_call_total_and_highest_rank(sql_results)

    if user_totals_and_highest_rank[0] > 10000:
        print("Players have a lot of points rn, that's crazy")

    print("High rank currently: ", user_totals_and_highest_rank[1])

    conn_total = n.call_neo_calc(neo_4j_results[1][3])

    print("Conn Total: ",conn_total)

    contents = f"""
    Highest Rank: {user_totals_and_highest_rank[1]}
    
    User Total: {user_totals_and_highest_rank[0]}
    
    Connection Total: {conn_total}
    """

    html_page = n.create_html("TOTALS", "Here are some helpful totals", contents)

    html_file = open("f.html", "w")
    html_file.write(html_page)
    html_file.close()

    return





if __name__ == "__main__":
    main()