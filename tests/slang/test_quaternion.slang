implementing glm_test;
import glm;

public glm.quat.quat test_identity()
{
    return glm.quat.identity();
}

public glm.quat.quat test_mul(glm.quat.quat a, glm.quat.quat b)
{
    return glm.quat.mul(a, b);
}

public glm.quat.quat test_conj(glm.quat.quat q)
{
    return glm.quat.conj(q);
}

public glm.quat.quat test_inv(glm.quat.quat q)
{
    return glm.quat.inv(q);
}

public glm.quat.quat test_from_axis_angle(float3 axisAngle)
{
    return glm.quat.fromAxisAngle(axisAngle);
}

public float3 test_as_axis_angle(glm.quat.quat q)
{
    return glm.quat.asAxisAngle(q);
}

public float3 test_rotate(glm.quat.quat q, float3 v)
{
    return glm.quat.rotate(q, v);
}

public float3x3 test_as_mat3(glm.quat.quat q)
{
    return glm.quat.asMat3(q);
}
