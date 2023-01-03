watch -n 0.5 "\
nvidia-smi -L;\
nvidia-smi;\
ps -up `nvidia-smi |tail -n +23 | head -n -1 | sed 's/\s\s*/ /g' | cut -d' ' -f5 | xargs`;\
"
