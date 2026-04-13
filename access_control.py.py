from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        return

    ip_packet = packet.find('ipv4')

    # Handle ARP packets
    if not ip_packet:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        return

    src = str(ip_packet.srcip)
    dst = str(ip_packet.dstip)

    # Allow h1 <-> h2 (both directions)
    if (src == "10.0.0.1" and dst == "10.0.0.2") or (src == "10.0.0.2" and dst == "10.0.0.1"):
        log.info("ALLOW %s -> %s", src, dst)

        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_NORMAL))
        event.connection.send(msg)

    else:
        log.info("BLOCK %s -> %s", src, dst)
        return

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)