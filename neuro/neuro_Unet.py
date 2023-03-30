import tensorflow as tf
CLASSES = 7

COLORS = ['green', 'turquoise', 'black', 'brown', 'blue', 'orange']

SAMPLE_SIZE = (256,256) # 1080 1920

OUTPUT_SIZE = (1080, 1920)


def load_images(image, mask):
    image = tf.io.read_file(image)
    image = tf.io.decode_jpeg(image)
    image = tf.image.resize(image, OUTPUT_SIZE)
    image = tf.image.convert_image_dtype(image, tf.float32)  # сверху вроде и так конв из uint8 в f32
    image = image / 255.0
    print(image)

    mask = tf.io.read_file(mask)
    mask = tf.io.decode_png(mask, channels=3)
    mask = tf.image.resize(mask, OUTPUT_SIZE)
    mask = tf.image.rgb_to_grayscale(mask)
    mask = tf.image.convert_image_dtype(mask, tf.float32)  # сверху вроде и так конв из uint8 в f32
    mask = mask / 255.0
    print(mask)

    masks = []

    for i in range(CLASSES):
        masks.append(tf.where(tf.equal(mask, float(i)), 1.0, 0.0))


    print(masks[3])


#with open("masks_machine/$image001.png") as f:

load_images("img_orig/$image001.jpg", "masks_machine/$image001.png")