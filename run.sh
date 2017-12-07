#if [ $stage -le 4 ]; then
  # later on we'll change this script so you have the option to
  # download the pre-built LMs from openslr.org instead of building them
  # locally.
  local/ted_train_lm.sh
#fi