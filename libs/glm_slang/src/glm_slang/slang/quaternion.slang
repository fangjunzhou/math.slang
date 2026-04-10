implementing glm;

namespace glm.quat
{

// Quaternions in glm.slang are defined as float4(x, y, z, w).
public typealias quat = float4;

// Returns the identity quaternion (1, 0, 0, 0).
public quat identity()
{
    return quat(0, 0, 0, 1);
}

// Multiplies two quaternions a and b, returning the result.
// @pram a The first quaternion.
// @pram b The second quaternion.
// @returns The product of the two quaternions.
[Differentiable]
public quat mul(quat a, quat b)
{
    float3 av = a.xyz;
    float3 bv = b.xyz;
    float aw = a.w;
    float bw = b.w;

    float3 v = aw * bv + bw * av + cross(av, bv);
    float w = aw * bw - dot(av, bv);
    return quat(v, w);
}

// Returns the complex conjugate of a quaternion q, which is defined as (-x, -y, -z, w).
// @param q The quaternion to conjugate.
// @returns The conjugate of the quaternion.
[Differentiable]
public quat conj(quat q)
{
    return quat(-q.xyz, q.w);
}

// Returns the inverse of a quaternion q. The inverse of a quaternion inv(q) is defined as a quaternion such that mul(q, inv(q)) = identity(). The inverse can be computed using the formula inv(q) = conj(q) / dot(q, q), where conj(q) is the conjugate of q and dot(q, q) is the squared magnitude of q.
// @param q The quaternion to invert.
// @returns The inverse of the quaternion.
[Differentiable]
public quat inv(quat q)
{
    return conj(q) / dot(q, q);
}

// Creates a quaternion from an axis and an angle.
// @param axisAngle A float3 where the direction of the vector represents the axis of rotation and the magnitude of the vector represents the angle of rotation in radians.
// @returns The quaternion representing the rotation.
[Differentiable]
public quat fromAxisAngle(float3 axisAngle)
{
    float angle = length(axisAngle);
    if (angle > 0)
    {
        axisAngle = normalize(axisAngle) * sin(angle * 0.5);
    }
    float w = cos(angle * 0.5);
    return quat(axisAngle, w);
}

// Converts a quaternion to an axis-angle representation. The returned float3 has a direction that represents the axis of rotation and a magnitude that represents the angle of rotation in radians.
// @param q The quaternion to convert.
// @returns A float3 representing the axis and angle of rotation.
[Differentiable]
public float3 asAxisAngle(quat q)
{
    float angle = 2 * acos(q.w);
    float s = length(q.xyz);
    if (s > 0)
    {
        return q.xyz / s * angle;
    }
    else
    {
        return float3(0, 0, 0);
    }
}

// Rotates a vector v by a quaternion q, returning the rotated vector.
// @param q The quaternion representing the rotation.
// @param v The vector to rotate.
// @returns The rotated vector.
[Differentiable]
public float3 rotate(quat q, float3 v)
{
    quat vQuat = quat(v, 0);
    quat result = mul(mul(q, vQuat), inv(q));
    return result.xyz;
}

// Converts a quaternion to a 3x3 rotation matrix. The resulting matrix can be used to rotate vectors in 3D space.
// @param q The quaternion to convert.
// @returns A 3x3 rotation matrix representing the same rotation as the quaternion.
[Differentiable]
public float3x3 asMat3(quat q)
{
    float3 rx = rotate(q, float3(1, 0, 0));
    float3 ry = rotate(q, float3(0, 1, 0));
    float3 rz = rotate(q, float3(0, 0, 1));
    return transpose(float3x3(rx, ry, rz));
}

}

