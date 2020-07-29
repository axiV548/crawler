# crawler

# taptap网站爬虫-taptap_comment


  ### 环境
  
    python 3.6.2
    scrapy 1.8

  ### 爬虫功能包括
  
    获取taptap所有的游戏id及信息
    
    根据游戏id获取游戏的所有评论（从1星到5星，每个游戏最多2500页评论，包含游戏id，用户名，用户id，评论，使用设备，游戏时间，被点欢乐数，被点赞数，被点踩数，楼中楼回复数）
    
    根据评论的用户id获取用户信息（包含用户名，用户id,签名，收到的赞，收到的欢乐，粉丝数，关注数，收藏数，玩过的游戏，玩得最久的游戏，评价数，贴子数，回复数）
    
    
  ### 目录结构
  
    ├── scrapy.cfg                  // scrapy入口
    └── taptap                      // 爬虫文件
        ├── __pycache__             //缓存
        ├── spiders
        │   ├── __pycache__          
        │   ├── __init__.py
        │   ├── game.py              //游戏信息爬虫
        │   ├── new.py               //测试文件
        │   ├── tap.py               //游戏评论爬虫
        │   └── user.py              //用户信息爬虫
        ├── __init__.py
        ├── items.py                 //数据容器
        ├── middlewares.py           //中间件
        ├── pipelines.py             //管道文件
        └── settings.py              //配置文件
        
  ### 使用方法及流程
  #### 数据表结构
    User{       //用户表
        recentplay{
          游戏ID = G_ID
          用户ID = U_ID
          游戏名称 = G_NAME
          游戏时长 = G_TIME
          类型标签 = T_TAGLIB
          G_NUMBER
        }
        tapuser{
          用户ID = U_ID
          用户名 = U_NAME
          粉丝数 = FANS
          关注数 = ATTENTION
          收藏数 = COLLECT
          玩过的游戏数 = PLAY
          玩的最久数 = L_PLAY
          评价数 = APPRAISE
        }
      }
      Game{         //游戏表
        游戏ID = G_ID
        游戏名称 = G_NAME
        简介 = BREIF
        最近更新内容 = R_CONTENT
        评论数量 = R_NUMBER
        社区数量 = C_NUMBER
        厂商 = VENDOR
        总评分 = A_DRADE
        类型标签 = T_TAGLIB
        编辑是否推荐 = RECOMMENT
        下载次数 = DOWNLOAD
        关注数 = ATTENTION
        图片路径 = URL
      }
      gametouser{     //游戏评论表
        评论ID = D_ID
        taptap用户 = U_ID
        对应游戏ID = G_ID
        用户名称 = U_NAME
        发布时间 = I_TIME
        评论星级 = D_STAR
        游戏时长 = G_TIME
        评论内容 = D_CONTENT
        游戏设备 = G_EQUIPTMENT
        欢乐数 = D_HAPPY
        点赞数 = D_AGRESS
        点踩数 = D_DISAGRESS
        回复数 = REPLY
      }
        
    爬虫使用pymysql连接数据库,除了游戏信息爬虫以外，其他爬虫输入数据都来自数据库
    
    在scrapy.cfg同级目录下运行"scrapy crawl game"遍历爬取从id=1到id=100000的游戏信息（可更改循环）
    
    运行"scrapy crawl tap -a gameNub=游戏id"替换游戏id爬取该游戏的评论信息
    
    运行"scrapy crawl user"爬虫会从数据库中查询用户id，并获取用户的信息（需使用cookie）
    
  
  
    
    
# Twitter图片爬虫
  使用selenium模拟请求控制chrome浏览器，通过给定关键字按照时间间隔来获取Twitter图片


# 微信公众号文章爬虫
  获取微信公众号所有的文章
  通过Fiddler获取微信电脑版客户端的请求key，将key填入WX.py的key变量，在有效期内就可以获取微信公众号的所有文章并转换为PDF格式保存到本地
  
  
