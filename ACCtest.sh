timeout -k 1m 1m ../MADP/src/solvers/GMAA -G FSPC -B BFS MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G kGMAA -B BFS MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G FSPC -B AM MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G kGMAA -B AM MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G FSPC -B CE MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G kGMAA -B CE MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G FSPC -B MP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G kGMAA -B MP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G FSPC -B BnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 1m 1m ../MADP/src/solvers/GMAA -G kGMAA -B BnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QPOMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QBG MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QMDPc MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QPOMDPav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QBGav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QHybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QPOMDPhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QBGhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QBGTreeIncPrune MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BFS -Q QBGTreeIncPruneBnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QPOMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QBG MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QMDPc MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QPOMDPav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QBGav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QHybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QPOMDPhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QBGhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QBGTreeIncPrune MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B AM -Q QBGTreeIncPruneBnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QPOMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QBG MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QMDPc MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QPOMDPav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QBGav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QHybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QPOMDPhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QBGhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QBGTreeIncPrune MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B CE -Q QBGTreeIncPruneBnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QPOMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QBG MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QMDPc MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QPOMDPav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QBGav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QHybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QPOMDPhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QBGhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QBGTreeIncPrune MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B MP -Q QBGTreeIncPruneBnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QPOMDP MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QBG MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QMDPc MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QPOMDPav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QBGav MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QHybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QPOMDPhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QBGhybrid MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QBGTreeIncPrune MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 5m 5m ../MADP/src/solvers/GMAA -G MAAstar -B BnB -Q QBGTreeIncPruneBnB MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
