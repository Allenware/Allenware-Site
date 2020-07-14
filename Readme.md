# MyBlog

[toc]



Allenware's personal blog source code.



## Blog



## Post

比起 Blog，更轻量，是类似微博、twitter、朋友圈之类的消息、照片推送分享。

### Model

- Post

  | Field        | Mean     | Type          |
  | ------------ | -------- | ------------- |
  | author       | 作者     | String        |
  | content      | 内容     | String        |
  | picture      | 文件     | File          |
  | status       | 状态     | int           |
  | like         | 喜欢数   | int           |
  | comment      | 评论     | Comment Model |
  | deliver_time | 发送时间 | datetime      |



