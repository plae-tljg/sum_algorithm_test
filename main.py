import exchange, cycle

node_names, weights = exchange.main()
cycle.find_cycles(node_names, weights)