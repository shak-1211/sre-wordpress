import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:151287120928:wordpress-notifications'
    post_data = json.loads(event['body'])
    post_title = post_data.get('post_title', 'New Post')
    message = f"New WordPress Post: {post_title}"
    sns.publish(TopicArn=topic_arn, Message=message)
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent')
    }
