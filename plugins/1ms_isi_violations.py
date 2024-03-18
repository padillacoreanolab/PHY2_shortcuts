# import from plugins/cluster_metrics.py
"""Show how to add a custom cluster metrics."""

import numpy as np
from phy import IPlugin


class ISIViolationPlugin1ms(IPlugin):
    def attach_to_controller(self, controller):
        """Note that this function is called at initialization time, *before* the supervisor is
        created. The `controller.cluster_metrics` items are then passed to the supervisor when
        constructing it."""

        def isi_violations(cluster_id):
            t = controller.get_spike_times(cluster_id).data

            all_isi = np.diff(t)
            return len(all_isi[all_isi < 0.0011])

        # Use this dictionary to define custom cluster metrics.
        # We memcache the function so that cluster metrics are only computed once and saved
        # within the session, and also between sessions (the memcached values are also saved
        # on disk).
        controller.cluster_metrics['1ms_isi'] = controller.context.memcache(isi_violations)