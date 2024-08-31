for dir in $(find . -type d); do
    if ! grep -Fxq "$dir" .gitignore && [ -f "$dir/README.md" ] && [[ $dir != *"/docs"* ]]; then
        newdir=$(echo "$dir" | sed "s/\./\.\/docs/")
        if [ ! -d "$newdir" ]; then
            mkdir -p "$newdir"
        fi
        cp "$dir/README.md" "$newdir/README.md"
    fi
done