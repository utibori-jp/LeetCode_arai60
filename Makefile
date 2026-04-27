start-new-problem:
	@read -p "ファイル名を入力してください: " dirName && \
	echo $$dirName && \
	cp -r template.md "$$dirName.md" && \
	echo "ファイルを作成しました。"
