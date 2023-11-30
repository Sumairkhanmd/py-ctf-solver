from typing import Literal

import beaker as bk
import pyteal as pt

from algokit_utils import (
    get_algod_client,
    get_default_localnet_config,
    get_algonode_config,
    get_account,
    ensure_funded,
    EnsureBalanceParameters,
    TestNetDispenserApiClient,
    ApplicationClient,
)
from algosdk.transaction import (
    wait_for_confirmation,
    ApplicationOptInTxn
)
from algosdk.util import algos_to_microalgos
from dotenv import load_dotenv


LEVEL_APP_ID=487250388 # TODO: fill in the app ID.


def main(network: Literal["localnet", "testnet"] = "localnet"):
    load_dotenv()

    if network == "localnet":
        algod = get_algod_client(get_default_localnet_config("algod"))
    elif network == "testnet":
        algod = get_algod_client(get_algonode_config("testnet", "algod", ""))
    else:
        raise ValueError(f"Unknown network: {network}")

    solver = get_account(algod, "SOLVER")

    if network == "localnet":
        ensure_funded(algod, EnsureBalanceParameters(
            account_to_fund=solver.address,
            min_spending_balance_micro_algos=algos_to_microalgos(10)
        ))
    elif network == "testnet":
        ensure_funded(algod, EnsureBalanceParameters(
            account_to_fund=solver.address,
            min_spending_balance_micro_algos=500_000,
            min_funding_increment_micro_algos=100_000,
            funding_source=TestNetDispenserApiClient()
        ))
    else:
        raise ValueError(f"Unknown network: {network}")

    # THIS IS AN EXAMPLE OF A BEAKER/PYTEAL APPLICATION. THIS IS NOT NEEDED FOR THIS LEVEL
    #  AND IT'S JUST FOR ILLUSTRATION PURPOSES.
    supporting_app = bk.Application("SupportingApp")

    @supporting_app.external
    def hello(name: pt.abi.String, *, output: pt.abi.String) -> pt.Expr:
        # Set output to the result of `Hello, `+name
        return output.set(pt.Concat(pt.Bytes("Hello, "), name.get()))

    supporting_app_spec = supporting_app.build(algod)
    supporting_app_client = ApplicationClient(algod, supporting_app_spec, signer=solver.signer)
    # END OF EXAMPLE APPLICATION

    wait_for_confirmation(
        algod,
        algod.send_transaction(
            ApplicationOptInTxn(
                solver.address,
                algod.suggested_params(),
                LEVEL_APP_ID
            ).sign(solver.private_key)
        )
    )
    
    print("success.")


if __name__ == "__main__":
    # main()
    main("testnet")
