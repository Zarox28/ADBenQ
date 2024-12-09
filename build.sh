if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  pyinstaller --distpath ./dist/linux adbenq.spec
elif [[ "$OSTYPE" == "darwin"* ]]; then
  pyinstaller --distpath ./dist/macos adbenq.spec
elif [[ "$OSTYPE" == "win32" ]]; then
  pyinstaller --distpath ./dist/windows adbenq.spec
fi