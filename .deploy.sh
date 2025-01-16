# Make sure pyproject.toml has an updates version code x.y.z
# Call this file as `./.deploy.sh x.y.z`

python3 -m build
twine check dist/wedme_plots-$1.tar.gz
twine upload dist/wedme_plots-$1.tar.gz