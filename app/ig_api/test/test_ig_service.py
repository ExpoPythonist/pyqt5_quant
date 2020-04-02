from ig_service import IGService

# from ig_service_config import *  # defines username, password, api_key, acc_type, acc_number
import pandas as pd

username = 'alinazay'
password = 'Koshenka98'
api_key = 'ca5adb0cc1a57f8a596e032f8b5b0a8864722b83'
acc_type = 'demo'


def test_ig_service():
    ig_service = IGService(username, password, api_key, acc_type)
    ig_service.create_session()

    print("fetch_accounts info")  # ****fetch_accounts info
    response = ig_service.fetch_accounts()
    print(response)
    assert (response['balance'][0]['available'] > 0)

    print("fetch_account_activity_by_period")
    """Returns the account activity history for the last specified period"""
    response = ig_service.fetch_account_activity_by_period(10000)
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_account_activity_by_period")
    response = ig_service.fetch_account_activity_by_period(10000)
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_transaction_history_by_type_and_period")
    """Returns the transaction history for the specified transaction type and period"""
    response = ig_service.fetch_transaction_history_by_type_and_period(10000, "ALL")
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_open_positions")
    response = ig_service.fetch_open_positions()
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_working_orders")
    """Returns all open working orders for the active account"""
    response = ig_service.fetch_working_orders()
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_top_level_navigation_nodes")
    """Returns all top-level nodes (market categories) in the market navigation hierarchy."""
    response = ig_service.fetch_top_level_navigation_nodes()
    print(response)  # dict with nodes and markets
    assert (isinstance(response, dict))
    market_id = response['nodes']['id'].iloc[0]

    print("fetch_client_sentiment_by_instrument")
    """Returns the client sentiment for the given instrument's market"""
    response = ig_service.fetch_client_sentiment_by_instrument(market_id)
    print(response)
    assert (isinstance(response, dict))

    print("fetch_related_client_sentiment_by_instrument")
    """Returns a list of related (also traded) client sentiment for the given instrument's market"""
    response = ig_service.fetch_related_client_sentiment_by_instrument(market_id)
    print(response)
    assert (isinstance(response, pd.DataFrame))

    print("fetch_sub_nodes_by_node")
    """Returns all sub-nodes of the given node in the market navigation hierarchy"""
    node = market_id  # ?
    response = ig_service.fetch_sub_nodes_by_node(node)
    print(response)

    # print("fetch_all_watchlists")
    # response = ig_service.fetch_all_watchlists()
    # print(response)
    # watchlist_id = response['id'].iloc[0]
    # # epic =
    #
    # print("fetch_watchlist_markets")
    # response = ig_service.fetch_watchlist_markets(watchlist_id)
    # print(response)
    # epic = response['epic'].iloc[0]
    #
    # print("fetch_market_by_epic")  # error from here......
    # response = ig_service.fetch_market_by_epic(epic)
    # print(response)
    #
    # print("search_markets")
    # search_term = 'UNDEF'
    # response = ig_service.search_markets(epic)
    # print(response)


    # print('sprintmarkets.......................')
    """Returns the client sentiment for the given instrument's market"""
    # create_open_position
    response = ig_service.create_open_position(
        currency_code="USD",
        direction="BUY",
        epic="IX.D.XINHUA.IFD.IP",
        expiry="-",
        force_open="true",
        guaranteed_stop="false",
        level=None,
        limit_distance=None,
        limit_level=None,
        order_type="MARKET",
        size="3",
        quote_id=None,
        stop_distance=None,
        stop_level=None)
    print('create_open_position ............',response)



test_ig_service()
