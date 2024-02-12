# Qiita Hackathonで作ったアプリのバックエンド
主にリアルタイム通信の処理に使用
## 使用技術
- FastAPI
- WebSocket

## WebSocket用のエンドポイント
### `/public/{room_name}`

このエンドポイントは、指定されたルーム内でのWebSocket通信を処理します。

### websoket/room_operations.py
- join_room
  ユーザーがチャットルームに参加するときに使用されます
- leave_room
  ユーザーがチャットルームから退出するときに使用されます
- send_message
  ユーザーがチャットルームにメッセージを送信するために使用されます

#### レスポンス
受け取ったデータを特定のルーム内の参加者に送信します。

- **userName**: 文字列。送信者のユーザー名。
- **message**: 文字列。送信されたメッセージの内容。
- **action**: 文字列。アクションの種類 (join、message、leave)。
