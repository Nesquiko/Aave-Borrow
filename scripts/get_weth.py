from scripts.util import get_account
from brownie import interface, config, network


def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])

    value = 0.1 * 10 ** 18
    tx = weth.deposit({"from": account, "value": value})
    tx.wait(1)

    return tx


def main():
    get_weth()
