# IBPhours

rotkonetworks hours worked on IBP related tasks. main focus on monitoring,
infrastructure tooling and keeping `config` repository up to date.
peers in the syndicate are encouraged to raise issue here or @matrix,
if anything is out of scope or hours wont match.

## Work Hours

| **Name** | **Month** | **Activity** | **Duration** | **Paid** | **Description** |
|----------|-----------|--------------|--------------|-----------------|----------------|
| Tommi    | Feb       | Mentoring    | 1 hour       | false | Mentored the Polkadot team on configuring and setting up HAProxy. |
| Tommi    | Apr       | Data Entry   | 1 hour       | false | Conducted data entry for missing service data as detailed in [GitHub Pull Request #41](https://github.com/ibp-network/config/pull/41). |
| Tommi    | Apr       | Tool Development | 6 hours   | false | Developed a tool to generate PeerIDs from secrets, available at [rotkonetworks/genpeerid](https://github.com/rotkonetworks/genpeerid). |
| Tommi    | Apr       | Debugging and Proposal Writing | 4 hours | false | Reviewed and contributed to the monitoring endpoint improvement proposal, detailed in [IBP Proposals #2](https://github.com/rotkonetworks/ibp-proposals/blob/master/proposals/2_monitoring_endpoints.md). |
| Tommi    | Apr       | Data Entry   | 5 hours       | false | Updated and audited bootnode data, including script writing for data identification and creating placeholders for absent entries. Contributions made to [Config PR #43](https://github.com/ibp-network/config/pull/43), [IBP Proposal #5](https://github.com/rotkonetworks/ibp-proposals/blob/master/proposals/5_bootnode_audits.md), and [Polkadot SDK PR #4276](https://github.com/paritytech/polkadot-sdk/pull/4276). |
| Tommi    | Apr       | Data Entry   | 5 hours       | false | Performed data entry related to adding localized service endpoints and filling in missing bootnode data as outlined in [PR#45](https://github.com/ibp-network/config/pull/45) and [PR#46](https://github.com/ibp-network/config/pull/46). |
| Tommi    | Apr       | Automation Development | 10 hours | false | Improved data integrity through the development of workflows that test endpoint archives, as shown in [PR#45](https://github.com/ibp-network/config/pull/45). |
| Tommi    | Apr       | Data Entry   | 5 hours       | false | Added external nodes to the repository, documented in [PR#47](https://github.com/ibp-network/config/pull/47). |
| Tommi    | Apr       | Monitoring Development | 26 hours | false | Developed initial code for bootnode and endpoint CI monitoring, and automated test workflows for bootnodes and endpoints, as recorded in [PR#47](https://github.com/ibp-network/config/pull/47) and [PR#48](https://github.com/ibp-network/config/pull/48) && review [PR #50](https://github.com/ibp-network/config/pull/50). |
| Tommi | May | Monitoring development | 16 hours | false | [PR #48](https://github.com/ibp-network/config/pull/48) Rework monitoring to use syndicate domain instead of individual domains with injected IP addresses. Add functionality to read SSL certs expiry date. |
| Tommi | May | Data entry | 1 hour | false | [wiki PR #17](https://github.com/ibp-network/wiki/pull/17) Write wiki entry about automated SSL cert fetching |
| Tommi | May | Monitoring development | 16 hours | false | Enhanced bootnode monitoring by implementing GNU parallel for task execution. Reduced the monitoring duration from approx 3 hours to a few minutes, enabling continuous monitoring and minimizing false positive alerts. Add alerts to endpoint+bootnode monitoring [PR #51](https://github.com/ibp-network/config). |

## Tracking method

Using [git hours](https://github.com/kimmobrunfeldt/git-hours) and forked/reworked [pomodoro script](https://github.com/rotkonetworks/ibphours) found in the `/scripts/` directory. each work hour contains 50m of
work and 10m of breaks.
to improve trackability, every worked half hour, changes are automatically
committed to this repository starting from May onwards. commit log based on 
focus.sh tool in scripts taking last line in `may.log`(expect chaos).
