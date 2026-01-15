from opentrons import protocol_api

metadata = {
    "protocolName": "Protocol Name",
    "author": "Codex",
    "description": "Short description",
    "apiLevel": "2.19",
}


def run(protocol: protocol_api.ProtocolContext):
    # TODO: load labware, modules, instruments, then implement liquid handling steps
    protocol.comment("Protocol start")

