import py_compile, zipfile, os, fnmatch

WOT_VERSION = "0.9.2"
CLIENT_PACKAGE_DIR = os.path.join("res_mods", WOT_VERSION, "scripts", "client")
BUILD_DIR = "build"
SRC_DIR = "src"
PACKAGE_NAME = "TessuMod.zip"

for root, dirs, files in os.walk(SRC_DIR):
	src_dir = root
	root2 = root[len(SRC_DIR)+1:]
	build_dir = os.path.join(BUILD_DIR, root2) if root2 else BUILD_DIR

	if not os.path.exists(build_dir):
		os.mkdir(build_dir)

	for filename in fnmatch.filter(files, "*.py"):
		filepath = os.path.join(root, filename)
		py_compile.compile(file=os.path.join(src_dir, filename), cfile=os.path.join(build_dir, filename)+"c", doraise=True)

if os.path.exists(PACKAGE_NAME):
	os.remove(PACKAGE_NAME)

fZip = zipfile.ZipFile(PACKAGE_NAME, "w")
for root, dirs, files in os.walk(BUILD_DIR):
	source_dir = root
	root2 = root[len(BUILD_DIR)+1:]
	target_dir = os.path.join(CLIENT_PACKAGE_DIR, root2)

	for filename in fnmatch.filter(files, "*.pyc"):
		fZip.write(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
fZip.close()